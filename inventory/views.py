from django.db.models import Q  # type: ignore
from django.shortcuts import get_object_or_404, redirect, render # type: ignore

from .forms import GroceryItemForm # type: ignore
from .models import GroceryItem

# Create your views here.
def item_list(request):
    items = GroceryItem.objects.all().order_by("-created_at")
    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()

    if search:
        items = items.filter(
            Q(name__icontains=search) | Q(notes__icontains=search)
        )

    if category:
        items = items.filter(category=category)

    if request.method == "POST":
        form = GroceryItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = GroceryItemForm()

    return render(
        request,
        "inventory/item_list.html",
        {
            "form": form,
            "items": items,
            "search": search,
            "selected_category": category,
            "categories": GroceryItem.CATEGORY_CHOICES,
        },
    )


def delete_item(request, item_id):
    item = get_object_or_404(GroceryItem, id=item_id)

    if request.method == "POST":
        item.delete()

    return redirect("item_list")