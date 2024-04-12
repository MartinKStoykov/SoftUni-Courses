function attachEvents() {
    const postsURL = "http://localhost:3030/jsonstore/blog/posts"
    const commentsURL = "http://localhost:3030/jsonstore/blog/comments"


    const loadPostsButton = document.getElementById("btnLoadPosts")
    const viewPostButton = document.getElementById("btnViewPost")

    const selectedPost = document.getElementById("posts")
    const postBody = document.getElementById("post-body")
    const postTitle = document.getElementById("post-title")
    const postedComments = document.getElementById("post-comments")

    let allObjPosts = {}

    loadPostsButton.addEventListener("click", async() => {
        selectedPost.innerHTML = ""
        const postsResponse = await fetch(postsURL)
        const posts = await postsResponse.json()
        allObjPosts = posts

        for (const post of Object.entries(posts)) {
            const optionElement = document.createElement("option")
            optionElement.textContent = post[1].title
            optionElement.value = post[0]

            selectedPost.appendChild(optionElement)
        }

    })
    viewPostButton.addEventListener("click", async () => {
        const postID = selectedPost.value

        postTitle.textContent = allObjPosts[0].title
        postBody.textContent = allObjPosts[0].body



        const commentsResponse = await fetch(commentsURL)
        const comments = await commentsResponse.json()
        postedComments.innerHTML = ""
        for (const value of Object.entries(comments)) {
            if (value[1].postId === postID) {
                const newLi = document.createElement("li")
                newLi.id = value[1].id
                newLi.textContent = value[1].text
                postedComments.appendChild(newLi)
            }
        }
    })
}

attachEvents();