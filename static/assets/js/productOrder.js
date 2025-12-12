let product_count = $("#product_count")

function add_to_basket(product_id) {
    $.get("/order/add_to_basket/", {
        "product_id": product_id,
        "product_count": product_count.val(),
    }).then(res => {
        if (res.status === "success") {
            swal.fire({
                position: "center",
                icon: "success",
                title: "محصول به سبد خرید اضافه شد",
            }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = "/order/cart/"
                    }
                }
            );
        }
        else if (res.status === "unauthorized") {
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
        } else if (res.status === "not_valid"){
            Swal.fire({
                position: "center",
                icon: "error",
                title: "مشکلی به وجود آمد",
            }).then((result)=>{
                if (result.isConfirmed) {
                    window.location.reload()
                }
            })
        }
    })
}