import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables (for API key)
load_dotenv()

# --- Configuration ---
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("Groq API key not found. Please set it in a '.env' file or as an environment variable (GROQ_API_KEY).")
    st.stop()

try:
    client = Groq(api_key=groq_api_key)
except Exception as e:
    st.error(f"Failed to initialize Groq client: {e}")
    st.stop()

# Groq model to use
# For good AI and speed, llama3-8b-8192 is a solid choice.
# For higher quality, consider 'llama3-70b-8192' but note the increased latency.
GROQ_MODEL = "llama-3.1-8b-instant" 

# --- Helper Function to Generate Content ---
def generate_content(product_name, product_category, key_features, target_audience, tone_of_voice, description_length, num_descriptions=2):
    """Generates product descriptions and hashtags using the Groq API."""
    
    # Adjust paragraph count based on selected length
    paragraph_map = {
        "Short (1 paragraph)": "1 paragraph",
        "Medium (2 paragraphs)": "2 paragraphs",
        "Long (3 paragraphs)": "3 paragraphs",
    }
    actual_description_length = paragraph_map.get(description_length, "2 paragraphs")

    prompt = f"""
    You are an expert product marketer and e-commerce copywriter. Your task is to create engaging, unique, and SEO-friendly product descriptions
    and a list of relevant hashtags for social media.

    Here are the product details:
    - **Product Name:** {product_name}
    - **Product Category:** {product_category}
    - **Key Features:**
    {key_features}
    - **Target Audience:** {target_audience}
    - **Tone of Voice:** {tone_of_voice}
    - **Desired Description Length:** {actual_description_length}

    Please generate {num_descriptions} distinct product description(s) that highlight the product's benefits,
    address the target audience's needs, and resonate with the specified tone.
    Each description should be approximately {actual_description_length} long.
    
    After each description, generate a comma-separated list of at least 10 relevant hashtags for social media,
    starting with '#'.

    Format your output clearly as follows:

    ---
    **Description 1:**
    [Generated Description 1 here]
    
    **Hashtags 1:** #[hashtag1], #[hashtag2], #[hashtag3], ...
    ---

    **Description 2:**
    [Generated Description 2 here]
    
    **Hashtags 2:** #[hashtag1], #[hashtag2], #[hashtag3], ...
    ---
    """
    
    messages = [
        {"role": "system", "content": "You are a helpful, creative, and experienced product marketer and e-commerce copywriter."},
        {"role": "user", "content": prompt}
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=GROQ_MODEL,
        temperature=0.8, # Slightly higher temperature for more creativity
        max_tokens=2048, 
    )
    return chat_completion.choices[0].message.content

# --- Streamlit UI ---
st.set_page_config(page_title="Product Marketer AI Assistant", page_icon="📈", layout="wide")

st.title("📈 Product Marketer AI Assistant")
st.markdown(f"""
Craft compelling product descriptions and social media hashtags instantly with the incredibly fast **Groq API**
powered by the **{GROQ_MODEL}** model. Perfect for product marketers!
""")

st.divider()

# --- Input Fields ---
with st.container(border=True):
    st.header("✍️ Product Details Input")

    col1, col2 = st.columns(2)
    with col1:
        product_name = st.text_input("Product Name", "Luxury Handcrafted Leather Wallet", help="e.g., 'Eco-Friendly Yoga Mat', 'Smart Home Security Camera'")
    with col2:
        product_category = st.text_input("Product Category", "Accessories", help="e.g., 'Electronics', 'Apparel', 'Home Decor'")
    
    key_features = st.text_area("Key Features (one per line)", 
                                """- Premium full-grain leather
- Hand-stitched for durability
- Slim design, holds 8 cards and cash
- RFID blocking technology
- Available in classic black and brown""",
                                help="List important features that differentiate your product. Be specific!")
    
    col3, col4 = st.columns(2)
    with col3:
        target_audience = st.text_input("Target Audience", "Discerning professionals, minimalist enthusiasts", help="Who is this product for? e.g., 'Gamers', 'Parents of toddlers', 'Outdoor adventurers'")
    with col4:
        tone_of_voice = st.selectbox("Tone of Voice", 
                                     ["Professional", "Friendly", "Luxurious", "Adventurous", "Playful", "Informative", "Persuasive", "Funny/Humor"],
                                     index=2, help="How should the description sound?")
    
    description_length = st.radio("Description Length", 
                                  ["Short (1 paragraph)", "Medium (2 paragraphs)", "Long (3 paragraphs)"], 
                                  index=1, horizontal=True)

    # Submit button
    generate_button = st.button("🚀 Generate Descriptions & Hashtags", use_container_width=True, type="primary")

st.divider()

# --- LLM Call and Output ---
if generate_button:
    if not product_name or not key_features:
        st.warning("Please provide at least a Product Name and Key Features to generate content.")
    else:
        with st.spinner(f"Creating content with {GROQ_MODEL}..."):
            try:
                generated_output = generate_content(
                    product_name, product_category, key_features, target_audience, tone_of_voice, description_length
                )
                st.session_state['generated_output'] = generated_output # Store in session state for regenerate/download
                st.session_state['product_name_for_download'] = product_name # Store product name for filename

                st.subheader("✨ Your Generated Content")
                st.markdown(generated_output)
                st.success("Content generated successfully!")

            except Exception as e:
                st.error(f"An error occurred during API call: {e}")
                st.warning("Please check your Groq API key and try again. You might also have reached your API rate limit or usage limits.")

# --- Regenerate and Download Buttons ---
if 'generated_output' in st.session_state and st.session_state['generated_output']:
    st.divider()
    col_reg_dl = st.columns(2)
    with col_reg_dl[0]:
        if st.button("🔄 Regenerate with Same Inputs", use_container_width=True):
            with st.spinner(f"Regenerating content with {GROQ_MODEL}..."):
                try:
                    generated_output = generate_content(
                        product_name, product_category, key_features, target_audience, tone_of_voice, description_length
                    )
                    st.session_state['generated_output'] = generated_output
                    st.subheader("✨ Your Regenerated Content")
                    st.markdown(generated_output)
                    st.success("Content regenerated successfully!")
                except Exception as e:
                    st.error(f"An error occurred during regeneration: {e}")
                    st.warning("Please check your Groq API key and try again.")
    
    with col_reg_dl[1]:
        # Create a downloadable text file
        filename = f"{st.session_state.get('product_name_for_download', 'product')}_descriptions_hashtags.txt"
        st.download_button(
            label="⬇️ Download Content",
            data=st.session_state['generated_output'].encode("utf-8"),
            file_name=filename,
            mime="text/plain",
            use_container_width=True
        )

st.markdown("---")
st.markdown("Made with ❤️ by an AI Enthusiast 🚀")
st.markdown("For internal use for product marketers use it to generate the content and then post it in social media. Always double-check generated content.")