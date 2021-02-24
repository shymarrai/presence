
const Modal = {
	
    open(id){
        //abrir modal
        //adicionar a classe active ao modal
        document
        .querySelector(".modal-overlay")
        .classList.add("active")
		Modal.presenceAdd(id)
    },
	
    close(){
        // fechar o modal de
        // remover a classe active do modal
        document
        .querySelector(".modal-overlay")
        .classList.remove("active")
		
    },

	presenceAdd(id){
		//const ausence = document.getElementById('ausenceButton') 
		
		const presence = document.getElementById('presenceButton')
		presence.addEventListener("click", function() {

			for(line of colaborator){
				if(id == line.id){
					let index = colaborator.indexOf(id)
					console.log(colaborator.splice(index,1))
					
				}
				//setInterval(function(){ window.location.reload() },1000)
				Modal.close()
				
			}
			alert("ok")
		})
		
		
		
	}


}
	
	
const Add = {
	Presence(){
		const presence = document.getElementById('presenceButton')
		presence.addEventListener("click", function() {
			let mat =  colaborator
		
			console.log(mat)
			mat = ''
				
		})
	}

}









const colaborator = [
	{
		name: "BRUNO FERNANDO GOMES DA SILVA",
		team: "C01",
		id: "2215035"
},
	{
		name: "JAILSON GOMES MARQUES CANDIDO",
		team: "C02",
		id: "2215074"
},
	{
		name: "ANDERSON MARCIO SILVA CASTILHO",
		team: "C03",
		id: "221501"
},
	{
		name: "ERIVELTON CONSTANTINO DE CARVALHO",
		team: "C04",
		id: "221987"
},
	{
		name: "MAURICIO MAGALHÃES DE MENDONSA",
		team: "C05",
		id: "125675"
},
	{
		name: "SEBASTIAO OCTAVIO DA SILVA NASCIMIENTO",
		team: "C06",
		id: "4568761"
},
];





const presence = [
{
		id: "2255671",
		name: "BRUNO FERNANDO GOMES DA SILVA",
		team: "C01",
},
];




const ausence = [
{
		id: "2255671",
		name: "BRUNO FERNANDO GOMES DA SILVA",
		team: "C01",
},
];





const Colabotators = {

		transactionsContainer: document.querySelector('#data-table tbody'),
		addTransaction(transaction, index){
			const tr = document.createElement('tr')
			tr.innerHTML = Colabotators.innerHTMLTransaction(transaction)
			tr.dataset.index = index
			Colabotators.transactionsContainer.appendChild(tr)
    
    },



		innerHTMLTransaction(transaction){

	    const html = `    
        <td colspan="5" class="name" onclick="">${transaction.name}</td>
        <td class="id">${transaction.id}</td>
        <td class="team">${transaction.team}</td>
        <td>
            <img style="cursor:pointer;"  onclick="Modal.open(${transaction.id})" src="./plus.svg" alt="Adicionar colaborador">
        </td>

        `

        return html
		},
		

	
}


const Presents = {
	/*     FOR OF PARA A LISTA PRESENCE*/
	transactionsPresence: document.querySelector('#data-presence tbody'),
	addPresence(colaborator, index){
	const tr = document.createElement('tr')
	tr.innerHTML = Presents.innerHTMLPresence(colaborator)
	tr.dataset.index = index
	Presents.transactionsPresence.appendChild(tr)

},
	
	innerHTMLPresence(row){
	const htmlPresence = `  
	<tr>      
	<td colspan="5" class="name" >${row.name}</td>
	<td class="id">${row.id}</td>
	<td class="team">${row.team}</td>
	<td>
		<img style="cursor:pointer;"  onclick="" src="./minus.svg" alt="Adicionar colaborador">
	</td>
	</tr>
	`
	return htmlPresence
	},

}




const Ausents = {
	/*     FOR OF PARA A LISTA PRESENCE*/
	transactionsAusents: document.querySelector('#data-ausence tbody'),
	addAusence(colaborator, index){
	const tr = document.createElement('tr')
	tr.innerHTML = Ausents.innerHTMLAusence(colaborator)
	tr.dataset.index = index
	Ausents.transactionsAusents.appendChild(tr)

},
	
	innerHTMLAusence(row){
	const htmlAusence = `  
	<tr>      
	<td colspan="5" class="name" >${row.name}</td>
	<td class="id">${row.id}</td>
	<td class="team">${row.team}</td>
	<td>
		<img style="cursor:pointer;"  onclick="" src="./minus.svg" alt="Adicionar colaborador">
	</td>
	</tr>
	`
	return htmlAusence
	},

}





const App = {
	
	init(){
		for(line of colaborator){
			Colabotators.addTransaction(line)
			
		}
		for(row of presence){
			Presents.addPresence(row)
			
		}
		for(row of ausence){
			Ausents.addAusence(row)
			
		}

	}



}

App.init();