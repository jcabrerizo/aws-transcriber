import logging
import jinja2


class HtmlFormatter:

    def __init__(self, model):
        self.model = model

    def format(self):
        html = jinja2.Environment(
            loader=jinja2.FileSystemLoader('./resources')
        ).get_template('template.jinja.html').render(
            title=self.model['title'],
            sentences=self.model['data']['sentences'],
            metadata=self.model['metadata']
        )

        return html
