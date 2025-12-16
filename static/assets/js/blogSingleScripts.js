let textarea = document.querySelector("#comment_text")

function send_comment(blog_id) {
    // event.preventDefault();
    let text = textarea.value
    $.post("/blog/send-comment/", {
        blog_id: blog_id,
        text: text
    }).done(function (res) {
            // if (res.status === "comment created") {
            let comments_section =
                Swal.fire({
                    position: "center",
                    icon: "success",
                    title: "کامنت شما بعد از تایید اضافه خواهد شد",
                }).then(() => {
                    $("#comments").html(res);
                    textarea.value = ""
                });
        }).fail(function (err) {
        Swal.fire({
            position: "center",
            icon: "error",
            title: "something went wrong!!!",
        });
    })
}
    // } else if (res.status === "error") {
    //     Swal.fire({
    //         position: "center",
    //         icon: "error",
    //         title: "something's wrong",
    //     });
    // } else {
    //     Swal.fire({
    //         position: "center",
    //         icon: "error",
    //         title: "something went wrong!!!",
    //     });
    // }



