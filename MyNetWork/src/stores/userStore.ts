import {defineStore} from "pinia"

export const useUserStore = defineStore("userStore", {
    state: () => {
        return {
            user: {
                id: -1,
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
                    if (data.length == 1) {
                        this.user.isLogged = true
                        this.user.pseudo = data[0]['pseudo']
                        this.user.email = data[0]['email']
                        this.user.urlImgProfil = data[0]['urlImgProfil']
                        this.user.id = data[0]['id']

                        this.set_cookies();
                    }
                })
        },
        get_cookies: async function () {
            if ($cookies.isKey('userId')) {
                this.user.isLogged = $cookies.get('userIsLogged')
                this.user.pseudo = $cookies.get('userPseudo')
                this.user.id = $cookies.get('userId')
                this.user.urlImgProfil = $cookies.get('userUrlImgProfile')
            }
        },
        set_cookies: function () {
            // Set cookies
            $cookies.set('userIsLogged', this.user.isLogged);
            $cookies.set('userPseudo', this.user.pseudo);
            $cookies.set('userEmail', this.user.email);
            $cookies.set('userId', this.user.id);
            $cookies.set('userUrlImgProfile', this.user.urlImgProfil);
        },
        logout: function () {
            this.user.isLogged = false;
            this.user.pseudo = "";
            this.user.email = "";
            this.user.urlImgProfil = "";
            this.user.id = -1;

            this.set_cookies();
        },
    }
})