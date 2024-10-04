function triggerGitHubAction() {
    const url = `https://api.github.com/repos/yourusername/yourrepo/dispatches`; // Replace with your repo URL
    const token = 'YOUR_GITHUB_TOKEN'; // Use a personal access token with repo scope

    fetch(url, {
        method: 'POST',
        headers: {
            'Authorization': `token ${token}`,
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            event_type: 'increment_click'
        }),
    })
    .then(response => {
        if (response.ok) {
            console.log('Workflow triggered successfully');
        } else {
            console.error('Error triggering workflow:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
}

// Call this function on button click
document.getElementById('downloadButton').addEventListener('click', triggerGitHubAction);
