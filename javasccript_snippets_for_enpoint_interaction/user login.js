function loginUser(username, password) {
    fetch('/login', { // Ensure you use the correct URL, e.g., https://yourdomain.com/login
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
        password: password
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data.message === "Login successful") {
        console.log("Login successful");
        // Handle successful login, like storing the session and redirecting the user
      } else {
        console.error("Login failed: " + data.message);
        // Handle login failure, show an error message to the user
      }
    })
    .catch(error => {
      console.error('Error during login:', error);
    });
  }
  