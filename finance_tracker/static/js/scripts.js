document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript connected!");
});
// script.js

const transactionsList = document.getElementById('transactions-list');
const addTransactionForm = document.getElementById('add-transaction-form');
const categorySelect = document.getElementById('category');
const amountInput = document.getElementById('amount');
const descriptionInput = document.getElementById('description');

const apiUrl = 'http://127.0.0.1:8000/api/';
const transactionsUrl = `${apiUrl}transactions/`;
const categoriesUrl = `${apiUrl}categories/`;

// Получение всех категорий для формы
async function getCategories() {
    const response = await axios.get(categoriesUrl);
    const categories = response.data;
    
    categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category.id;
        option.textContent = category.name;
        categorySelect.appendChild(option);
    });
}

// Получение всех транзакций
async function getTransactions() {
    const response = await axios.get(transactionsUrl);
    const transactions = response.data;

    transactionsList.innerHTML = ''; // Очищаем список
    transactions.forEach(transaction => {
        const transactionElement = document.createElement('div');
        transactionElement.classList.add('transaction');
        transactionElement.innerHTML = `
            <h3>${transaction.category.name}</h3>
            <p>Amount: $${transaction.amount}</p>
            <p>${transaction.description}</p>
            <p>Date: ${new Date(transaction.date).toLocaleDateString()}</p>
        `;
        transactionsList.appendChild(transactionElement);
    });
}

// Отправка формы для добавления транзакции
addTransactionForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const newTransaction = {
        category: categorySelect.value,
        amount: parseFloat(amountInput.value),
        description: descriptionInput.value,
    };

    await axios.post(transactionsUrl, newTransaction);
    getTransactions(); // Обновляем список транзакций
});

// Инициализация
getCategories();
getTransactions();
