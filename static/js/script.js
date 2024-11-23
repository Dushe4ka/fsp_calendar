document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.menu-bar');
    const timebtn = document.querySelectorAll('.filter-time');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Удаляем активный класс у всех вкладок
            tabs.forEach(item => item.classList.remove('active'));
            
            // Добавляем активный класс текущей вкладке
            tab.classList.add('active');
        });
    });
    timebtn.forEach(btn => {
        btn.addEventListener('click', () => {
            // Удаляем активный класс у всех вкладок
            timebtn.forEach(item => item.classList.remove('active'));
            
            // Добавляем активный класс текущей вкладке
            btn.classList.add('active');
        });
    });
});