import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  const [isNavVisible, setIsNavVisible] = useState(false);
  const [errorMessage, setErrorMessage] = useState(""); // State to handle potential error messages

  // Function to toggle the navigation visibility with basic error handling
  const toggleNav = () => {
    try {
      setIsNavVisible(!isNavVisible);
    } catch (error) {
      console.error("Failed to toggle navigation:", error);
      setErrorMessage("An error occurred while trying to toggle the navigation. Please try again.");
    }
  };

  return (
    <header>
      <nav>
        {errorMessage && <p className="error-message">{errorMessage}</p>} {/* Display error message if any */}
        <div className="mobile-nav">
          <button onClick={toggleNav}>{isNavVisible ? 'Close' : 'Menu'}</button>
        </div>
        {isNavVisible && (
          <ul>
            <li><Link to="/" onClick={toggleNav}>Home</Link></li>
            <li><Link to="/about" onClick={toggleNav}>About</Link></li>
            <li><Link to="/services" onClick={toggleNav}>Services</Link></li>
            <li><Link to="/contact" onClick={toggleNav}>Contact</Link></li>
          </ul>
        )}
      </nav>
    </header>
  );
};

export default Header;