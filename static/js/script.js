
// Target the thead elements, assign them as HTML attributes to data cells
var headertext = [];
var headers = document.querySelectorAll("thead");
var tablebody = document.querySelectorAll("tbody");

for (let i = 0; i < headers.length; i++) {
    headertext[i]=[];
    for (let j = 0, headrow; headrow = headers[i].rows[0].cells[j]; j++) {
        let current = headrow;
        headertext[i].push(current.textContent);
    }
   }

for (let h = 0, tbody; tbody = tablebody[h]; h++) {
    for (let i = 0, row; row = tbody.rows[i]; i++) {
        for (let j = 0, col; col = row.cells[j]; j++) {
            col.setAttribute("data-th", headertext[h][j]);
        }
    }
  }

