const express = require('express');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.json());

app.post('/save', (req, res) => {
    const habitData = req.body;
    fs.writeFile('habit.json', JSON.stringify(habitData), (err) => {
        if (err) {
            res.status(500).json({ message: 'Error al guardar los datos.' });
        } else {
            res.json({ message: 'Datos guardados correctamente.' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
