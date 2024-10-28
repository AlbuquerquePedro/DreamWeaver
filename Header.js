import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  // State to handle the toggle for mobile navigation
  const [isNavVisible, setIsNavVisible] = useState(false);

  // Function to toggle the navigation visibility
  const toggleNav = () => {
    setIsNavVisible(!isNavVisible);
  };

  return (
    <header>
      <nav>
        <div className="mobile-nav">
          {/* Mobile navigation toggle button */}
          <button onClick={toggleNav}>{isNavVisible ? 'Close' : 'Menu'}</button>
        </div>
        {/* Conditionally render navigation items if isNavVisible is true */}
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