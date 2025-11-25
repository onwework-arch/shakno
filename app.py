import streamlit as st
from engine.batch import generate_batch_async, generate_batch_sync
from engine.generator import generate_single_post
from engine.utils import ensure_dir
import os

st.set_page_config(page_title='ShakNow Pro', layout='centered')
st.title('ShakNow Pro — Ultra AI CMS')

st.markdown('Enter a long-tail topic and generate SEO-optimized posts (drafts go to WordPress).')

topic = st.text_input('Topic', value='Samsung S24 Review')
word_goal = st.number_input('Target word count', min_value=1500, max_value=5000, value=2500, step=100)
meta_description = st.text_area(
    'SEO meta tag description',
    value='',
    placeholder='Optional: describe the key takeaway, CTA, or keyword focus for this post.',
    help='Leave blank to auto-generate, or supply a custom meta description for SERP snippets.',
)

cols = st.columns(2)
with cols[0]:
    publish = st.checkbox('Publish to WordPress (draft)', value=True)
with cols[1]:
    async_run = st.checkbox('Run in background', value=False)

st.markdown('---')
if st.button('Generate 1 SEO post'):
    ensure_dir('outputs')
    st.info(f'Starting generation of 1 post for: {topic} (target ~{word_goal} words)')
    if async_run:
        generate_batch_async(
            topic,
            count=1,
            publish=publish,
            meta_description=meta_description or None,
            word_count=word_goal,
        )
        st.success('Post queued in background. Check outputs/ and WP drafts shortly.')
    else:
        results = generate_batch_sync(
            topic,
            count=1,
            publish=publish,
            meta_description=meta_description or None,
            word_count=word_goal,
        )
        st.success(f'Post complete. Generated {len(results)} item.')
        for r in results:
            st.write(f"- {r['title']} → {r['html']} | WP ID: {r.get('wp_id')} | Words: {r.get('word_count')}")

st.markdown('---')
st.header('Generate single post')
single_topic = st.text_input('Single topic', value='Samsung S24 Camera Review')
if st.button('Generate Single'):
    res = generate_single_post(
        single_topic,
        publish=publish,
        meta_description=meta_description or None,
        word_count=word_goal,
    )
    st.success(f"Generated: {res['title']} → {res['html']} | WP ID: {res.get('wp_id')} | Words: {res.get('word_count')}")
    st.write(res)
