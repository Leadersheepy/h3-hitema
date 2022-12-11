import {defineStore} from "pinia"

export const useUserStore = defineStore("userStore", {
    state: () => {
        return {
            user: {
                id: 0,
                isLogged: false,
                pseudo: "",
                email: "",
                urlImgProfil: ""
            },
        }
    },
    actions: {
        add: async function (identifiant) {

            return {message: "ok"};
        },
        login: function (identifiants) {
            fetch(`http://localhost:3000/utilisateurs?email=${identifiants.email}&password=${identifiants.password}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    if (data.length == 1) {
                        this.user.isLogged = true
                        this.user.pseudo = data[0]['pseudo']
                        this.user.email = data[0]['email']
                        this.user.urlImgProfil = data[0]['urlImgProfil']
                        this.user.id = data[0]['id']

                        // Set cookies
                        $cookies.set('userIsLogged', true)
                        $cookies.set('userPseudo', data[0]['pseudo'])
                        $cookies.set('userId', data[0]['id'])
                        $cookies.set('userUrlImgProfile', data[0]['urlImgProfil'])
                    }
                })
        },
        get_cookie: async function () {
            if ($cookies.isKey('userId')) {
                this.user.isLogged = true
                this.user.pseudo = $cookies.get('userPseudo')
                this.user.id = $cookies.get('userId')
                this.user.urlImgProfil = $cookies.get('userUrlImgProfile')
            }
        },
        logout: function () {
        },
    }

})