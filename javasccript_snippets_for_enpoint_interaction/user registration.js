function registerUser(username, password) {
    fetch('/register', { // Ensure you use the correct URL, e.g., https://yourdomain.com/register
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
      if (data.message === "User registered successfully") {
        console.log("Registration successful");
        // Handle successful registration, possibly redirect or login the user
      } else {
        console.error("Registration failed: " + data.message);
        // Handle registration failure
      }
    })
    .catch(error => {
      console.error('Error during registration:', error);
    });
  }
  