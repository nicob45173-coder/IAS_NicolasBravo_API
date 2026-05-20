async function cargarUsuarios() {
    const res = await fetch('/users');
    const data = await res.json();

    const lista = document.getElementById("lista");
    lista.innerHTML = "";

    data.forEach(user => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${user.name}
            <button onclick="eliminar(${user.id})">X</button>
        `;
        lista.appendChild(li);
    });
}

async function crearUsuario() {
    const name = document.getElementById("name").value;

    await fetch('/users', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name})
    });

    cargarUsuarios();
}

async function eliminar(id) {
    await fetch(`/users/${id}`, { method: "DELETE" });
    cargarUsuarios();
}

cargarUsuarios();