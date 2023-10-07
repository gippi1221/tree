from django import template
from core.models import TreeMenu
from django.urls import resolve

register = template.Library()

def collect_tree(menu_name, parent=None):
    menu_items = TreeMenu.objects.filter(parent=parent, name=menu_name)
    print(menu_items)
    tree = []
    for item in menu_items:
        children = collect_tree(menu_name, item)
        tree.append({'item': item, 'children': children})
    return tree

@register.inclusion_tag('menu_template.html')
def draw_menu(request, name):
    current_url = resolve(request.path_info).url_name
    
    tree = collect_tree(name)
    print(tree)
    return {'menu_items': tree}