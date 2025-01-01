function getCsrfToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}

document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function() {
        const postId = this.dataset.postId;

        fetch(`/post/${postId}/like`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                const likeCountElement = this.closest('.post').querySelector('.like-count');
                likeCountElement.textContent = data.like_count;

                this.textContent = data.liked ? 'Unlike' : 'Like';
            }
        })
        .catch(err => console.error('Error:', err));
    });
});
