const searchField = document.querySelector('#searchField');
const paginationContainer = document.querySelector(".pagination-container");
const tBody = document.querySelector(".t-body");
const tableOutput = document.querySelector('.table-output');
tableOutput.style.display= "none";
const appTable = document.querySelector('.app-table');



searchField.addEventListener('keydown', (e) => {

    const searchValue = e.target.value;

    if (searchValue.trim().length > 0) {
        paginationContainer.style.display = "none";
        tBody.innerHTML = "";
        // console.log('searchValue', searchValue);

        fetch("/income/search_income", {
                body: JSON.stringify({
                    searchText: searchValue
                }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                appTable.style.display = "none";
                tableOutput.style.display = "block";

                if (data.length === 0) {
                    tableOutput.innerHTML = 'No resule found';
                    tableOutput.style.display="none";
                }else {
                    data.forEach((item) => {
                        tBody.innerHTML += `
                        <tr>
                            <td>${item.amount}</td>
                            <td>${item.source}</td>
                            <td>${item.descriptions}</td>
                            <td>${item.date}</td>
                        </tr>`;

                    });
                }
            });
    } else {
        appTable.style.display = "block";
        tableOutput.style.display = "none";
        paginationContainer.style.display = "block";

    }
});