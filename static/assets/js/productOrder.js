let cart_content = $("#cart_orders_container")

function add_to_basket(product_id) {
    let product_count = $("#product_count")
    $.get("/order/add_to_basket/", {
        "product_id": product_id,
        "product_count": product_count.val(),
    }).then(res => {
        if (res.status === "success") {
            swal.fire({
                position: "center",
                icon: "success",
                showDenyButton: true,
                confirmButtonText: "بله",
                denyButtonText: "خیر",
                title: "محصول به سبد خرید اضافه شد",
                text: "میخواهید به سبد خرید بروید؟"
            }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = "/order/cart/"
                    } else if (result.isDenied) {
                        window.location.reload()
                    }
                }
            );
        } else if (res.status === "unauthorized") {
            Swal.fire({
                position: "center",
                icon: "warning",
                title: "ابتدا باید وارد حساب کاربری خود شوید",
            }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = "/user/login-register/"
                    }
                }
            );
        } else if (res.status === "not_valid") {
            Swal.fire({
                position: "center",
                icon: "error",
                title: "مشکلی به وجود آمد",
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.reload()
                }
            })
        }
    })
}

function increase_quantity(product_id) {
    $.get("/order/increase-quantity/", {
        "product_id": product_id
    }).then(
        res => {
            if (res.status === "increase") {
                cart_content.html(res.content)
            }
        }
    )
}

function decrease_quantity(product_id) {
    $.get("/order/decrease-quantity/", {
        "product_id": product_id
    }).then(res => {
        if (res.status === "decrease") {
            cart_content.html(res.content)
        } else if (res.status === "remove") {
            swal.fire({
                position: "center",
                icon: "warning",
                showDenyButton: true,
                confirmButtonText: "بله",
                denyButtonText: "خیر",
                title: "میخواهید این محصول را حذف کنید؟",
            }).then((result) => {
                    if (result.isConfirmed) {
                        delete_item(product_id)
                    } else if (result.isDenied) {

                    }
                }
            );
        }
    })
}

function delete_item(product_id) {
    $.get("/order/delete-item/", {
        "product_id": product_id
    }).then(res => {
        cart_content.html(res.content)
    })
}
