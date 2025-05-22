import React from 'react';
import './MainContent.css';

const MainContent = () => {
  return (
    <main>
      <section className="welcome-section">
        <h2>Experience the Taste of Brazil!</h2>
        <p>
          Authentic Brazilian steakhouse experience with a variety of grilled meats,
          fresh salads, and traditional side dishes. Come and enjoy the rodizio
          style service where our gauchos will bring a parade of succulent meats
          right to your table.
        </p>
        <img 
          src="https://via.placeholder.com/800x400?text=Delicious+Churrasco" 
          alt="Delicious Churrasco" 
          className="main-image"
        />
      </section>

      <section className="specials-section">
        <h3>Our Meats</h3>
        <ul>
          <li>Picanha (Top Sirloin Cap)</li>
          <li>Fraldinha (Flank Steak)</li>
          <li>Cordeiro (Lamb)</li>
          <li>Alcatra (Top Sirloin)</li>
          <li>Costela de Porco (Pork Ribs)</li>
        </ul>
      </section>
    </main>
  );
};

export default MainContent;
