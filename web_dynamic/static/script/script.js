var proClickLink = document.querySelector('.pro_click');
var profileList = document.querySelector('.profile_list');

// Define the event handler function
function handleClick() {
    // Toggle the display property of the profile list
    profileList.style.display = (profileList.style.display === 'none') ? 'block' : 'none';
};

// Attach the event listener to the pro_click link
proClickLink.addEventListener("click", handleClick);