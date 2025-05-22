import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header>
      <h1>Churrascaria Deluxe</h1>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/menu">Menu</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
