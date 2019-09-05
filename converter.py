class Converter:
    @staticmethod
    def convert_tags(content):
        ul = '<div style="display: block; list-style-type: disc; margin-block-start: 1em; margin-block-end: 1em; margin-inline-start: 0px; margin-inline-end: 0px; padding-inline-start: 40px;">'
        ol = '<div style="display: block; list-style-type: decimal; margin-block-start: 1em; margin-block-end: 1em; margin-inline-end: 0px; padding-inline-start: 40px;">'
        li = '<div style="display: list-item; text-align: -webkit-match-parent;">'

        new_content = content.replace('<ul>', ul).replace('<ol>', ol).replace('<li>', li).replace('</ul>', '</div>').replace('</ol>', '</div>').replace('</li>', '</div>')

        return new_content