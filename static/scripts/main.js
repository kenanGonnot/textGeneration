const lengthInput = document.getElementById('temperature');
const lengthOutput = document.getElementById('value');

lengthInput.addEventListener('input', (event) => {
    lengthOutput.textContent = event.target.value;
});

const generatedText = document.getElementById('generated_text');
const text = generatedText.innerText;
generatedText.innerText = '';

let i = 0;
const intervalId = setInterval(() => {
    if (i >= text.length) {
        clearInterval(intervalId);
    } else {
        const char = text[i];
        if (char === ' ') {
            generatedText.innerHTML += '&nbsp;';
        } else {
            generatedText.innerText += char;
        }
        i++;
    }
}, 50);

// $(document).ready(function () {
//     $('form').on('submit', function (event) {
//         event.preventDefault();  // Empêche le formulaire de recharger la page
//
//         $.ajax({
//             type: 'POST',
//             url: '/',
//             data: $('text_generator').serialize(),  // Récupère les données du formulaire
//             success: function (generated_text) {
//                 // Affiche la réponse dans la div ayant l'id "response"
//                 $('#generated_text').html(generated_text);
//             }
//         });
//     });
// });


// $(document).ready(function () {
//     $('#text_generator').submit(function (event) {
//         event.preventDefault();
//         var input_text = $('#input_text').val();
//         $.ajax({
//             url: '/generated',
//             type: 'POST',
//             data: {input_text: input_text},
//             success: function (response) {
//                 $('#generated_text').text(response.generated_text);
//             },
//             error: function (error) {
//                 console.log(error);
//             }
//         });
//     });
// });

// // Récupérer le formulaire et le champ de texte
// const form = document.getElementById("text-generator");
// const textOutput = document.getElementById("generated_text");
//
// // Ajouter un écouteur d'événement pour le formulaire
// form.addEventListener("submit", (event) => {
//     event.preventDefault(); // Empêcher le rechargement de la page
//
//     // Récupérer les données du formulaire
//     const formData = new FormData(form);
//     const textLength = formData.get("text_length");
//     const model = formData.get("model");
//
//     // Envoyer une requête AJAX à l'API OpenAI
//     fetch("/generated", {
//         method: "POST",
//         body: formData,
//     })
//         .then((response) => response.text())
//         .then((generatedText) => {
//             // Afficher le texte généré
//             textOutput.innerText = generatedText;
//         })
//         .catch((error) => {
//             console.error(error);
//         });
// });
