document.addEventListener('DOMContentLoaded', function() {
  const leftButton = document.querySelector('.left-scroll-cards');
  const rightButton = document.querySelector('.right-scroll-cards');
  const cardsContainer = document.querySelector('.food-list .container');
  const cards = document.querySelectorAll('.food-list_card');

  let currentIndex = 0;
  let cardWidth = cards[0].offsetWidth + 40; // Ширина карточки с учетом зазора

  // Обработчик нажатия на кнопку "вправо"
  rightButton.addEventListener('click', () => {
      if (currentIndex < cards.length - 1) {
          currentIndex++;
          updateScrollPosition();
      }
  });

  // Обработчик нажатия на кнопку "влево"
  leftButton.addEventListener('click', () => {
      if (currentIndex > 0) {
          currentIndex--;
          updateScrollPosition();
      }
  });

  // Обновление положения прокрутки контейнера
  function updateScrollPosition() {
      cardWidth = cards[currentIndex].offsetWidth + 40;
      const newPosition = currentIndex * cardWidth;
      cardsContainer.scrollTo({
          left: newPosition,
          behavior: 'smooth'
      });
  }
});
