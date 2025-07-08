
document.querySelectorAll('.number-input').forEach(wrapper => {
    const input = wrapper.querySelector('input[type="number"]');
    const increment = wrapper.querySelector('.increment');
    const decrement = wrapper.querySelector('.decrement');

    increment.addEventListener('click', () => {
        input.stepUp();
    });

    decrement.addEventListener('click', () => {
        input.stepDown();
    });
});