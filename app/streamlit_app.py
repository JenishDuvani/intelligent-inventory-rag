# import streamlit as st
# from chunker import block_chunking, page_chunking
# from utils import read_uploaded_file
# from ingestion_pipeline import index_chunks
# from chat_engine import generate_answer

# st.set_page_config(page_title="Inventory RAG Assistant", layout="wide")

# # ---------- SESSION STATE ----------
# if "current_page" not in st.session_state:
#     st.session_state.current_page = "chat"

# if "metadata" not in st.session_state:
#     st.session_state.metadata = {}

# if "raw_text" not in st.session_state:
#     st.session_state.raw_text = None

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "selected_model" not in st.session_state:
#     st.session_state.selected_model = "us.anthropic.claude-3-5-haiku-20241022-v1:0"

# # ---------- SIDEBAR ----------
# with st.sidebar:
#     st.title("📦 Inventory RAG")

#     if st.button("📄 Upload / Manage Documents"):
#         st.session_state.current_page = "upload"
#         st.rerun()

#     st.divider()

#     if st.button("💬 Back to Chat"):
#         st.session_state.current_page = "chat"
#         st.rerun()

# # ---------- CHAT PAGE ----------
# if st.session_state.current_page == "chat":

#     st.title("💬 Chat With Your Documents")

#     model_options = {
#     "Claude Sonnet 4": "us.anthropic.claude-sonnet-4-20250514-v1:0",
#     "Claude Sonnet 4.5": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
#     "Claude Sonnet 4.6": "us.anthropic.claude-sonnet-4-6",
#     # "Claude Opus 4": "us.anthropic.claude-opus-4-20250514-v1:0",
#     "Claude Opus 4.1": "us.anthropic.claude-opus-4-1-20250805-v1:0",
#     "Claude Opus 4.5": "us.anthropic.claude-opus-4-5-20251101-v1:0",
#     "Claude Opus 4.6": "us.anthropic.claude-opus-4-6-v1"
# }

#     top_col1, top_col2 = st.columns([3, 1])

#     with top_col2:
#         selected_model_name = st.selectbox(
#             "Model",
#             list(model_options.keys())
#         )
#         st.session_state.selected_model = model_options[selected_model_name]

#     st.divider()

#     if not st.session_state.chat_history:
#         st.info("Upload and index documents first from the sidebar.")

#     for chat in st.session_state.chat_history:
#         with st.chat_message("user"):
#             st.markdown(chat["question"])

#         with st.chat_message("assistant"):
#             st.markdown(chat["answer"])

#     user_query = st.chat_input("Ask a question about your indexed documents...")

#     if user_query:
#         with st.chat_message("user"):
#             st.markdown(user_query)

#         with st.spinner("Searching and generating answer..."):
#             answer = generate_answer(
#                 user_query,
#                 model_id=st.session_state.selected_model
#             )

#         with st.chat_message("assistant"):
#             st.markdown(answer)

#         st.session_state.chat_history.append(
#             {
#                 "question": user_query,
#                 "answer": answer
#             }
#         )

# # ---------- DOCUMENT PAGE ----------
# if st.session_state.current_page == "upload":

#     st.title("📄 Upload & Index Documents")

#     uploaded_file = st.file_uploader(
#         "Upload CSV or TXT file",
#         type=["csv", "txt"]
#     )

#     if uploaded_file:
#         st.session_state.raw_text = read_uploaded_file(uploaded_file)
#         st.success(f"Loaded: {uploaded_file.name}")

#     st.subheader("Metadata")

#     col1, col2 = st.columns(2)

#     with col1:
#         meta_key = st.text_input("Metadata Key")

#     with col2:
#         meta_value = st.text_input("Metadata Value")

#     if st.button("➕ Add Metadata"):
#         if meta_key and meta_value:
#             st.session_state.metadata[meta_key] = meta_value

#     if st.session_state.metadata:
#         st.markdown("#### Current Metadata")

#         for key in list(st.session_state.metadata.keys()):
#             c1, c2 = st.columns([4, 1])

#             with c1:
#                 st.write(f"{key}: {st.session_state.metadata[key]}")

#             with c2:
#                 if st.button("❌", key=f"delete_{key}"):
#                     del st.session_state.metadata[key]
#                     st.rerun()

#     st.subheader("Chunking")

#     chunking_type = st.radio(
#         "Chunking Method",
#         ["Block-based", "Page-based"]
#     )

#     if chunking_type == "Block-based":
#         chunk_size = st.slider("Chunk Size", 200, 1000, 500)
#         overlap = st.slider("Overlap", 0, 300, 100)
#     else:
#         delimiter = st.text_input("Page Delimiter", value="---PAGE---")

#     if st.session_state.raw_text and st.button("🚀 Index Document"):

#         if chunking_type == "Block-based":
#             chunks = block_chunking(
#                 text=st.session_state.raw_text,
#                 chunk_size=chunk_size,
#                 overlap=overlap,
#                 metadata=st.session_state.metadata
#             )
#         else:
#             chunks = page_chunking(
#                 text=st.session_state.raw_text,
#                 page_delimiter=delimiter,
#                 metadata=st.session_state.metadata
#             )

#         with st.spinner("Generating embeddings and indexing document..."):
#             result = index_chunks(chunks)

#         st.success("Document indexed successfully")
#         st.json(result)

#         if st.button("➡ Go To Chat"):
#             st.session_state.current_page = "chat"
#             st.rerun()
import streamlit as st
from chunker import block_chunking, page_chunking
from utils import read_uploaded_file
from ingestion_pipeline import index_chunks
from chat_engine import generate_answer

st.set_page_config(page_title="Inventory RAG Assistant", layout="wide")

# ---------- SESSION STATE ----------
if "current_page" not in st.session_state:
    st.session_state.current_page = "chat"

if "metadata" not in st.session_state:
    st.session_state.metadata = {}

if "raw_text" not in st.session_state:
    st.session_state.raw_text = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"

if "saved_prompts" not in st.session_state:
    st.session_state.saved_prompts = {
        "Inventory Analyst": """You are an intelligent inventory and demand forecasting assistant.

Focus on:
- Inventory shortages
- Overstock risks
- Supplier delays
- Demand forecasting
- Suggested business actions""",

        "Supplier Communication": """You are a supplier communication assistant.

Focus on:
- Supplier delays
- Shipment issues
- Replenishment suggestions
- Drafting procurement-related explanations""",

        "Demand Forecasting": """You are a demand forecasting expert.

Focus on:
- Demand changes
- Seasonal patterns
- Region-wise demand growth
- Future inventory planning"""
    }

if "selected_prompt_name" not in st.session_state:
    st.session_state.selected_prompt_name = "Inventory Analyst"

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("📦 Inventory RAG")

    if st.button("💬 Chat"):
        st.session_state.current_page = "chat"
        st.rerun()

    if st.button("📄 Upload / Manage Documents"):
        st.session_state.current_page = "upload"
        st.rerun()

    if st.button("🧠 Manage Prompt Templates"):
        st.session_state.current_page = "prompts"
        st.rerun()

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# ---------- CHAT PAGE ----------
if st.session_state.current_page == "chat":

    st.title("💬 Chat With Your Documents")

    model_options = {
    "Claude Sonnet 4": "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "Claude Sonnet 4.5": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "Claude Sonnet 4.6": "us.anthropic.claude-sonnet-4-6",
    # "Claude Opus 4": "us.anthropic.claude-opus-4-20250514-v1:0",
    "Claude Opus 4.1": "us.anthropic.claude-opus-4-1-20250805-v1:0",
    "Claude Opus 4.5": "us.anthropic.claude-opus-4-5-20251101-v1:0",
    "Claude Opus 4.6": "us.anthropic.claude-opus-4-6-v1"
}

    top_col1, top_col2 = st.columns([3, 1])

    with top_col2:
        selected_model_name = st.selectbox(
            "Model",
            list(model_options.keys())
        )
        st.session_state.selected_model = model_options[selected_model_name]

    prompt_names = list(st.session_state.saved_prompts.keys())

    selected_prompt_name = st.selectbox(
        "Prompt Template",
        prompt_names,
        index=prompt_names.index(st.session_state.selected_prompt_name)
    )

    st.session_state.selected_prompt_name = selected_prompt_name

    st.divider()

    if not st.session_state.chat_history:
        st.info("Upload and index documents first from the sidebar.")

    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(chat["question"])

        with st.chat_message("assistant"):
            st.markdown(chat["answer"])

    user_query = st.chat_input("Ask a question about your indexed documents...")

    if user_query:
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.spinner("Searching and generating answer..."):
            answer = generate_answer(
                user_query,
                model_id=st.session_state.selected_model,
                system_prompt=st.session_state.saved_prompts[
                    st.session_state.selected_prompt_name
                ]
            )

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.chat_history.append(
            {
                "question": user_query,
                "answer": answer
            }
        )

# ---------- DOCUMENT PAGE ----------
if st.session_state.current_page == "upload":

    st.title("📄 Upload & Index Documents")

    uploaded_file = st.file_uploader(
        "Upload CSV or TXT file",
        type=["csv", "txt"]
    )

    if uploaded_file:
        st.session_state.raw_text = read_uploaded_file(uploaded_file)
        st.success(f"Loaded: {uploaded_file.name}")

    st.subheader("Metadata")

    col1, col2 = st.columns(2)

    with col1:
        meta_key = st.text_input("Metadata Key")

    with col2:
        meta_value = st.text_input("Metadata Value")

    if st.button("➕ Add Metadata"):
        if meta_key and meta_value:
            st.session_state.metadata[meta_key] = meta_value

    if st.session_state.metadata:
        st.markdown("#### Current Metadata")

        for key in list(st.session_state.metadata.keys()):
            c1, c2 = st.columns([4, 1])

            with c1:
                st.write(f"{key}: {st.session_state.metadata[key]}")

            with c2:
                if st.button("❌", key=f"delete_{key}"):
                    del st.session_state.metadata[key]
                    st.rerun()

    st.subheader("Chunking")

    chunking_type = st.radio(
        "Chunking Method",
        ["Block-based", "Page-based"]
    )

    if chunking_type == "Block-based":
        chunk_size = st.slider("Chunk Size", 200, 1000, 500)
        overlap = st.slider("Overlap", 0, 300, 100)
    else:
        delimiter = st.text_input("Page Delimiter", value="---PAGE---")

    if st.session_state.raw_text and st.button("🚀 Index Document"):

        if chunking_type == "Block-based":
            chunks = block_chunking(
                text=st.session_state.raw_text,
                chunk_size=chunk_size,
                overlap=overlap,
                metadata=st.session_state.metadata
            )
        else:
            chunks = page_chunking(
                text=st.session_state.raw_text,
                page_delimiter=delimiter,
                metadata=st.session_state.metadata
            )

        with st.spinner("Generating embeddings and indexing document..."):
            result = index_chunks(chunks)

        st.success("Document indexed successfully")
        st.json(result)

        if st.button("➡ Go To Chat"):
            st.session_state.current_page = "chat"
            st.rerun()

# ---------- PROMPT MANAGEMENT PAGE ----------
if st.session_state.current_page == "prompts":

    st.title("🧠 Manage Prompt Templates")

    prompt_names = list(st.session_state.saved_prompts.keys())

    selected_prompt_name = st.selectbox(
        "Choose Prompt Template",
        prompt_names,
        index=prompt_names.index(st.session_state.selected_prompt_name)
    )

    st.session_state.selected_prompt_name = selected_prompt_name

    selected_prompt_text = st.session_state.saved_prompts[selected_prompt_name]

    edited_prompt = st.text_area(
        "Prompt Content",
        value=selected_prompt_text,
        height=300
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("💾 Update Prompt"):
            st.session_state.saved_prompts[selected_prompt_name] = edited_prompt
            st.success("Prompt updated")

    with col2:
        new_prompt_name = st.text_input("New Prompt Name")

        if st.button("➕ Save New Prompt"):
            if new_prompt_name:
                st.session_state.saved_prompts[new_prompt_name] = edited_prompt
                st.session_state.selected_prompt_name = new_prompt_name
                st.success("New prompt saved")
                st.rerun()

    with col3:
        if (
            st.button("🗑 Delete Prompt")
            and selected_prompt_name not in [
                "Inventory Analyst",
                "Supplier Communication",
                "Demand Forecasting"
            ]
        ):
            del st.session_state.saved_prompts[selected_prompt_name]
            st.session_state.selected_prompt_name = "Inventory Analyst"
            st.success("Prompt deleted")
            st.rerun()