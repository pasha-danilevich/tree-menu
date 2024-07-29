from django import template
from django.template.loader import render_to_string

from tree_menu_app.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_identifier):
    current_path = context['request'].path
    menu_items = MenuItem.objects.filter(menu_name=menu_identifier).prefetch_related('childrens', 'parent')

    list_items = list(menu_items)
    active_item = next((item for item in list_items if item.url == current_path), None)

    # Получаем корневые элементы (родителей)
    root_items = [item for item in list_items if item.parent is None]

    # Список ID развернутых элементов
    expanded_ids = []

    if active_item:
        # Получаем всех родителей выделенного элемента
        expanded_ids = collect_expanded_ids(active_item)

    # Добавляем дочерние элементы к родителям
    for parent in root_items:
        if parent.id in expanded_ids:
            parent.child_items = collect_child_items(list_items, parent.id, expanded_ids)

    result_context = {'items': root_items, 'current_path': current_path}
    
        
    return render_to_string('menu.html', result_context)

def collect_expanded_ids(active_item):
    expanded_ids = []
    current_node = active_item
    while current_node:
        expanded_ids.append(current_node.id)
        current_node = current_node.parent
    return expanded_ids

def collect_child_items(list_items, parent_id, expanded_ids):
    children = [
        item for item in list_items if item.parent_id == parent_id
    ]
    for child in children:
        if child.id in expanded_ids:
            child.child_items = collect_child_items(list_items, child.id, expanded_ids)
    return children

