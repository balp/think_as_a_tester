from pyramid.view import view_config

from .storage import seen_passages


@view_config(route_name="home", renderer="think_as_tester:templates/mytemplate.jinja2")
def my_view(request):
    return {"station": "Station One",
            "lorries": seen_passages.lorries,
            "tons": seen_passages.tons,
            }


