const testDataInput = document.getElementById("testDataInput");
const resultSpan = document.getElementById("result");

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
                    const confidence = response.confidence;
                    const result = response.result;
                    resultSpan.innerText = `The value ${value} is considered ${result} with confidence ${confidence}.`
                }
                else {
                    resultSpan.innerText = response.message;
                }
            });
    }
}