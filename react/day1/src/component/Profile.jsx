

function Profile() {
    const user = {
        name: "Ajitesh Mishra",
        gmail: "ajitesh@gmail.com",
        address: {
            city: "Chitrakoot",
            pincode: '210209'
        }
    }
    const {name, gmail, address:{city, pincode}} = user;

    return (
        <div>
            <h3>Hi {name} here How can i help you</h3>
            <h4>If any query: {gmail}</h4>
            <h4>Our Office location: `({city} { pincode})`</h4>
        </div>
    );
    
}

export default Profile;