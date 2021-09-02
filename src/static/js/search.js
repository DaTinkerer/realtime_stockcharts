const app = new Vue({
  delimiters: ["[", "]"],
  el: "#app",
  data: {
    userInput: "",
    datas: [],
  },

  methods: {
    queryTheSymbol() {
      axios({
        method: "GET",
        url: `https://api.twelvedata.com/symbol_search?
                apikey=xxx&outputsize=6&symbol=${this.userInput}`,
      })
        .then((response) => {
          this.datas = response.data.data;
        })
        .then(() => {
          dataList = document.querySelector(".data-list");

          this.datas.forEach((element) => {
            // If element.symbol is already inside of dataList.innerHTML do not
            // add the same symbol again.
            if (dataList.innerHTML.includes(element.symbol) == false) {
              dataList.innerHTML += `<option value=${element.symbol}>`;
            }
          });
        })

        .catch((err) => {
          console.log(err);
        });
    },
  },
});
