// When a "View More" button is clicked
document.querySelectorAll('.view-more').forEach(button => {
    button.addEventListener('click', function() {
        const projectId = this.getAttribute('data-id'); // Get the project ID
        fetch(`/project-details/${projectId}`) // Fetch detailed info from the server
            .then(response => response.json()) // Convert the response to JSON
            .then(data => {
                // Display detailed info in the project-details div
                document.getElementById('project-details').innerHTML = `
                    <h1>${data.title}</h1>
                    <p>${data.description}</p>
                    <p>${data.category}</p>
                    <p>${data.technologies}</p>
                    <img src="${data.screenshot_url}" alt="Screenshot of ${data.title}">
                    <p>${data.features}</p>
                    <p>${data.challenges}</p>
                    <p><a href="${data.url}">Project URL</a></p>
                    <p><a href="${data.repository_url}">Repository URL</a></p>
                    <p>Created at: ${data.created_at}</p>
                    <p>Updated at: ${data.updated_at}</p>
                `;
            });
    });
});
