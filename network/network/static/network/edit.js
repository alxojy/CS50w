function edit(id) {
    var edit_box = document.querySelector(`#edit-box-${id}`);
    var edit_btn = document.querySelector(`#edit-btn-${id}`);
    edit_box.style.display = 'block';
    edit_btn.style.display = 'block';

    edit_btn.addEventListener('click', () => {
        fetch('/edit/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                post: edit_box.value
            })
          });
        
          edit_box.style.display = 'none';
          edit_btn.style.display = 'none';

          document.querySelector(`#post-${id}`).innerHTML = edit_box.value;
    });

    edit_box.value = "";
}

function like(id) {
    var like_btn = document.querySelector(`#like-btn-${id}`);
    var like_ct = document.querySelector(`#like-count-${id}`);

    like_btn.addEventListener('click', () => {

        if (like_btn.style.backgroundColor == 'white') {
            fetch('/like/' + id, {
                method: 'PUT',
                body: JSON.stringify({
                    like: true
                })
              })

            like_btn.style.backgroundColor = 'red';
              
            fetch('/like/'+ id)
            .then(response => response.json())
            .then(post => {
                like_ct.innerHTML = post.likes;
            });
        }
        else {
            fetch('/like/' + id, {
                method: 'PUT',
                body: JSON.stringify({
                    like: false
                })
              });
              
            like_btn.style.backgroundColor = 'white';

            fetch('/like/'+`${id}`)
            .then(response => response.json())
            .then(post => {
                like_ct.innerHTML = post.likes;
            });
        }
        return false;
    });

}