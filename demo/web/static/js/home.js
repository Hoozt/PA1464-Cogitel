const testDataInput = document.getElementById("testDataInput");
const resultSpan = document.getElementById("result");
console.log(resultSpan);

const uploadData = () => {
    console.log("Function uploadData() is not yet implemented.");
}

const testData = () => {
    const value = testDataInput.value;
    if(value) {
        fetch("api/predict/" + value)
            .then(response => {
                return response.json();
            }).then(response => {
                const status = response.status
                if (status === "ok") {
                    const value = response.value;
                    const valueStatus = response.valueStatus;
                    resultSpan.innerText = `The value ${value} is considered ${valueStatus}.`
                }
                else {
                    resultSpan.innerText = `Illegal input`
                }
            });
    }
}