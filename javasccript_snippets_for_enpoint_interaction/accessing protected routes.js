function fetchProtectedData() {
    fetch('/protected', { // Ensure you use the correct URL, e.g., https://yourdomain.com/protected
      method: 'GET',
      credentials: 'include' // This is required to include the session cookie in the request
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Not authorized to access this resource');
      }
    })
    .then(data => {
      console.log("Protected data:", data);
      // Handle the protected data
    })
    .catch(error => {
      console.error('Error accessing protected route:', error);
    });
  }
  