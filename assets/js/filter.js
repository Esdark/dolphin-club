const filters = document.querySelector("#filters");

filters.addEventListener("input", filterGoods);

function filterGoods() {
  const Materials = filters.querySelector("#Materials").value,
    sizes = [...filters.querySelectorAll("#size input:checked")].map(
      (n) => n.value
    ),
    priceMin = document.querySelector("#price-min").value,
    priceMax = document.querySelector("#price-max").value;

  outputGoods(
    DATA.filter(
      (n) =>
        (!Materials || n.Materials === Materials) &&
        (!sizes.length || sizes.includes(n.size)) &&
        (!priceMin || priceMin <= n.cost) &&
        (!priceMax || priceMax >= n.cost)
    )
  );
}

function outputGoods(goods) {
  document.getElementById("goods").innerHTML = goods
    .map(
      (n) => `
    <div class="single-goods">
    <div class="border-2 border-gray-200 rounded-lg overflow-hidden mb-3">
      <div class="text-center">
      <h3 class"py-2 font-bold">${n.name}</h3>
      <img src="${n.image}" class="block mx-auto">
      <p class="font-bold py-4">Цена: ${n.cost}</p>
      
      <div class="overflow-hidden flex justify-center p-8">
  <button tabindex="-1" data-art="${n.name}" class="focus:outline-none w-32 py-2 rounded-md font-semibold text-white bg-indigo-500 ring-4 ring-indigo-300 hover:bg-indigo-700">
    Button
  </button>
</div>
      </div>
      </div>
    </div>
  `
    )
    .join("");
}

const DATA = [
  {
    sex: "male",
    name: "Materials 1",
    cost: 1000,
    Materials: "Materials 3",
    image:
      "https://www.okboss.co.in/assets/img/home/boysrow1/kids%20musterd%20jacket%20with%20white%20tshirt%20party%20wear%20dress.jpg",
    size: "S",
  },
  {
    sex: "male",
    name: "Materials 1",
    cost: 1200,
    Materials: "Materials 1",
    image:
      "https://www.okboss.co.in/assets/img/home/boysrow1/kids%20musterd%20jacket%20with%20white%20tshirt%20party%20wear%20dress.jpg",
    size: "M",
  },
  {
    sex: "male",
    name: "Materials 1",
    cost: 1700,
    Materials: "Materials 2",
    image:
      "https://www.okboss.co.in/assets/img/home/boysrow1/kids%20musterd%20jacket%20with%20white%20tshirt%20party%20wear%20dress.jpg",
    size: "L",
  },
  {
    sex: "male",
    name: "Materials 1",
    cost: 2000,
    Materials: "Materials 1",
    image:
      "https://www.okboss.co.in/assets/img/home/boysrow1/kids%20musterd%20jacket%20with%20white%20tshirt%20party%20wear%20dress.jpg",
    size: "XL",
  },
];

outputGoods(DATA);
