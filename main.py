from website import create_app
from flask import request, jsonify
from seo_checker import SEOChecker
import requests
import re

app = create_app()
seo = SEOChecker()


@app.route("/process_keywords", methods=["POST"])
def process_keywords():
    data = request.get_json()
    user_keywords = data.get("user_keywords")
    try:
        keyword_suggestions = seo.get_keyword_suggestions(user_keywords)
    except Exception as e:
        return jsonify({"error": "Pri spracovaní kľúčových slov sa vyskytla chyba"}), 500

    return jsonify(keyword_suggestions=keyword_suggestions)


@app.route("/process_url", methods=["POST"])
def process_url():
    data = request.get_json()
    url = data.get("url")

    try:
        # Regex na kontrolu formatu URL
        if re.match(r"^(http|https)://", url):

            # Kontrola dostupnosti URL
            requests.head(url)

            title_tag_result = seo.check_title_tag_length(url)
            favicon_result = seo.check_favicon(url)
            meta_description_result = seo.check_meta_description_length(url)
            meta_keywords_result = seo.check_meta_keywords(url)
            https_result = seo.check_https(url)
            url_length_result = seo.check_url_length(url)
            url_format_result = seo.check_url_format(url)
            url_versions_result = seo.check_url_versions(url)
            viewport_meta_tag_result = seo.check_viewport_meta_tag(url)
            robots_meta_tag_result = seo.check_robots_meta_tag(url)
            lang_attribute_result = seo.check_lang_attribute(url)
            hreflang_attribute_result = seo.check_hreflang_attribute(url)
            canonical_link_result = seo.check_canonical_link(url)
            noindex_attribute_result = seo.check_noindex_attribute(url)
            noindex_header_result = seo.check_noindex_header(url)
            open_graph_result = seo.check_open_graph(url)
            schema_markup_result = seo.check_schema_markup(url)
            robots_txt_result = seo.check_robots_txt(url)
            sitemap_xml_result = seo.check_sitemap_xml(url)
            h1_presence_result = seo.check_h1_presence(url)
            h2_tags_result = seo.check_h2_tags(url)
            heading_tag_hierarchy_result = seo.check_heading_tag_hierarchy(url)
            image_attributes_result = seo.check_image_attributes(url)
            alt_attributes_result = seo.check_alt_attributes(url)
            form_field_labels_result = seo.check_form_field_labels(url)
            button_accessibility_result = seo.check_button_accessibility(url)
            text_to_html_ratio_result = seo.check_text_to_html_ratio(url)
            w3c_validity_result = seo.check_w3c_validity(url)
            dom_elements_result = seo.check_dom_elements(url)
            iframes_result = seo.check_iframes(url)
            inline_css_result = seo.check_inline_css(url)
            page_size_result = seo.check_page_size(url)
            page_objects_result = seo.check_page_objects(url)
            custom_404_page_result = seo.check_custom_404_page(url)
            ga_tag_result = seo.check_ga_tag(url)
            plaintext_emails_result = seo.check_plaintext_emails(url)
            gzip_enabled_result = seo.check_gzip_enabled(url)
            media_queries_result = seo.check_media_queries(url)
            character_encoding_declaration_result = (seo.check_character_encoding_declaration(url))
            meta_refresh_tag_result = seo.check_meta_refresh_tag(url)
            aria_attributes_result = seo.check_aria_attributes(url)
            minified_css_result = seo.check_minified_css(url)
            page_speed_data_result = seo.get_page_speed_data(url)
            image_size_result = seo.check_image_size(url)
            broken_links_result = seo.check_broken_links(url)

            results = [
                title_tag_result,
                favicon_result,
                meta_description_result,
                meta_keywords_result,
                https_result,
                url_length_result,
                url_format_result,
                url_versions_result,
                viewport_meta_tag_result,
                robots_meta_tag_result,
                lang_attribute_result,
                hreflang_attribute_result,
                canonical_link_result,
                noindex_attribute_result,
                noindex_header_result,
                open_graph_result,
                schema_markup_result,
                robots_txt_result,
                sitemap_xml_result,
                h1_presence_result,
                h2_tags_result,
                heading_tag_hierarchy_result,
                image_attributes_result,
                alt_attributes_result,
                form_field_labels_result,
                button_accessibility_result,
                text_to_html_ratio_result,
                w3c_validity_result,
                dom_elements_result,
                iframes_result,
                inline_css_result,
                page_size_result,
                page_objects_result,
                custom_404_page_result,
                ga_tag_result,
                plaintext_emails_result,
                gzip_enabled_result,
                media_queries_result,
                character_encoding_declaration_result,
                meta_refresh_tag_result,
                aria_attributes_result,
                minified_css_result,
                page_speed_data_result,
                image_size_result,
                broken_links_result,
            ]

            return jsonify(results=results)

        else:

            return jsonify({"error": "URL musí začínať s https:// alebo http://"}), 400

    except Exception as e:
        return jsonify({"error": "Nepodarilo sa načítať adresu URL."}), 400


if __name__ == "__main__":
    app.run(debug=False)
