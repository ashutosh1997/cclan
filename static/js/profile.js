$(document).ready(function(){
    $("#edit-pic").hide();
    $("#edit-cover").hide();
});

$(document).ready(function(){

    $("#profile-image-container").hover(function(){
        $("#edit-pic").show();
    });
    $("#profile-image-container").mouseleave(function(){
        $("#edit-pic").hide();
    });

    $("#cover-image").hover(function(){
        $("#edit-cover").show();
    });
    $("#cover-image").mouseleave(function(){
        $("#edit-cover").hide();
    });
});


function showPreview(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#avatar-preview').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#avatar").change(function(){
        showPreview(this);
    });

function coverPreview(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#cover-preview').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#cover").change(function(){
        coverPreview(this);
    });

function postImagePreview(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#post-image-preview').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#post_image").change(function(){
        postImagePreview(this);
    });