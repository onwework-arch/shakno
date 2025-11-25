import os
import markdown
from .seo_generator import (
    generate_focus_keyword,
    generate_meta_description,
    generate_long_content,
)
from .interlinker import build_internal_links
from .affiliate import inject_affiliates
from .images import fetch_image_suggestion
from .publisher import publish_to_wordpress
from .templates import render
from .utils import slug, save_output, read_yaml

CONFIG = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'wp_config.yaml'))


def generate_single_post(topic, publish=False, affiliate=True, meta_description=None, word_count=2500):
    """
    Generates one post for `topic`.
    Returns dict: title, md path, html path, wp_id, links
    """
    # create stable slug base to avoid collisions
    key_slug = slug(topic)
    # SEO components
    keyword = generate_focus_keyword(topic)
    meta = generate_meta_description(topic, override=meta_description)
    blocks = generate_long_content(topic, target_words=word_count)
    # prepare related candidates for interlinking
    candidates = [f"{topic} {s}" for s in ['Specs', 'Camera', 'Battery', 'Reviews', 'Accessories', 'Comparison', 'User Experience']]
    internal_links = build_internal_links(topic, candidates)
    # affiliate section
    cfg = read_yaml(CONFIG)
    affiliate_section = ''
    if affiliate and cfg:
        affiliate_template = cfg.get('affiliate_template')
        if affiliate_template:
            affiliate_section = inject_affiliates('Buy here: {AFFILIATE_PLACEHOLDER}', affiliate_template)
    # image suggestion
    image = fetch_image_suggestion(topic)
    # render markdown via template
    md = render('blog.md.j2',
                title=topic,
                keyword=keyword,
                meta_description=meta,
                intro=blocks.get('intro', ''),
                features=blocks.get('features', ''),
                review=blocks.get('review', ''),
                pros=blocks.get('pros', ''),
                cons=blocks.get('cons', ''),
                specs=blocks.get('specs', ''),
                comparisons=blocks.get('comparisons', ''),
                faqs=blocks.get('faqs', ''),
                internal_links=internal_links,
                affiliate_section=affiliate_section,
                image=image,
                conclusion=blocks.get('conclusion', ''))
    # ensure unique output folder by appending incremental suffix only if folder exists
    base_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'outputs'))
    target_dir = os.path.join(base_dir, key_slug)
    suffix = 0
    final_dir = target_dir
    while os.path.exists(final_dir):
        suffix += 1
        final_dir = f"{target_dir}-{suffix}"
    os.makedirs(final_dir, exist_ok=True)
    md_path = os.path.join(final_dir, f"{key_slug}.md")
    html_path = os.path.join(final_dir, f"{key_slug}.html")
    save_output(md_path, md)
    # convert to html and save
    html = markdown.markdown(md, extensions=['fenced_code', 'tables'])
    save_output(html_path, html)
    # try publish if requested
    wp_id = None
    if publish:
        try:
            wp_id = publish_to_wordpress(topic, html, meta, publish=False)
        except Exception as e:
            wp_id = {'error': str(e)}
    return {'title': topic, 'md': md_path, 'html': html_path, 'wp_id': wp_id, 'links': internal_links, 'meta_description': meta, 'word_count': word_count}
