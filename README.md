<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Index</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-qKXV1j0HvMUeCBQ+QVp7JcfGl760yU08IQ+GpUo5hlbpg51QRiuqHAJz8+BrxE/N"
    crossorigin="anonymous"></script>

  <style>
    main {
      background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("../img/log.jpg");
      background-size: cover;


    }

    #inform {
      display: flex;
      align-items: center;
      padding: 20px 0px 30px 0px;
    }

    #sobre {
      display: flex;
      flex-direction: column;
      padding: 20px 90px 20px 90px;
      gap: 16px;
    }

    #sobre h1 {
      font-weight: 900;
      color: #EFBC75;
      font-size: 60px;
      line-height: 67px;
    }

    #sobre h2 {
      font-weight: 700;
      color: #C1E1A7;
      font-size: 34px;
      line-height: 42px;
    }

    #sobre h3 {
      font-weight: 400;
      color: #cdd8c4;
      font-size: 19px;
      line-height: 21px;
      width: auto;
    }

    #sobre h4 {
      font-weight: 500;
      color: #dcdddc;
      font-size: 12px;
      line-height: 11px;
      width: auto;
    }

    #codigo {
      margin: 40px 60px 60px 80px;
      opacity: 0.8;
    }

    #codigo pre {
      filter: blur(1px);
      opacity: 0.8;
    }

    #codigo pre::after {
      content: "|";
      opacity: 1;
      margin-left: 5px;
      display: inline-block;
      animation: blink .7s infinite;
    }

    @keyframes blink {

      0%,
      100% {
        opacity: 1;
      }

      50% {
        opacity: 0;
      }
    }


    #historia {
      background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("../img/icono.jpg");
      background-size: cover;
      border-top: 2px solid #1A4A5A;
      border-bottom: 2px solid #1A4A5A;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 50px 80px;
      gap: 20px;
    }

    #historia h1 {
      text-align: center;
      font-weight: 400;
      font-size: 24px;
      line-height: 25px;
      color: #fff;
    }

    @media screen and (max-width: 910px) {

      #inform {
        display: flex;
        align-items: center;
        flex-direction: column;
      }
    }

      @media screen and (max-width: 768px) {
        #codigo {
          margin-left: 40px;
          font-size: 15px;
        }

      }

      @media screen and (max-width: 770px) {


        #sobre {
          padding: 60px;
        }

        #sobre h1 {
          font-size: 40px;
        }

        #sobre h2 {
          font-size: 26px;
        }

        #sobre h3 {
          font-size: 17px;
          margin-right: 20px;
        }

        #codigo {
          margin: 0;
          margin-left: 0px;
        }

        #codigo pre {
          filter: blur(0);
          opacity: 0.5;
        }

        #codigo span {
          font-size: 8px;
          padding-left: 0px;
        }

        #historia img {
          margin-right: 110px;
        }

        #historia h1 {
          font-size: 20px;
          margin-right: 50px;
        }

        #historia {
          display: flex;
          flex-direction: column;
          padding: 50px 0px 50px 60px;
        }

      }

      @media screen and (max-width: 450px) {
        #sobre {
          padding: 20px 0px 20px 30px;
          gap: 8px;
        }

        #sobre h1 {
          font-size: 35px;
        }

        #sobre h2 {
          font-size: 24px;
        }
      }
  </style>


</head>

<body class="bg-black bg-gradient">

  <header>
    <div class="px-3 py-2 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a href="/" class="d-flex align-items-center my-2 my-lg-0 me-lg-auto text-white text-decoration-none">
            <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap">
              <img src="https://rqueaarequipa.github.io/img/logo.png" alt="" width="20%">
            </svg>
          </a>

          <ul class="nav col-12 col-lg-auto my-2 justify-content-center my-md-0 text-small">
            <li>
              <a href="#" class="nav-link text-secondary">
                Home
              </a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                Formularios
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Formulario Encuesta</a></li>
                <li><a class="dropdown-item" href="#">Formulario Operaciones Aritmeticas</a></li>
                <li>
                </li>
                <li><a class="dropdown-item" href="#">Formulario Calculo Volumen</a></li>
              </ul>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                Respuestas
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Respuesta de Encuesta</a></li>
                <li><a class="dropdown-item" href="#">Respuesta de Operaciones Aritmeticas</a></li>
                <li>
                </li>
                <li><a class="dropdown-item" href="#">Respuesta de Calculo Volumen</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>
  <div class="bg-dark bg-gradient">
    <div class="container">
      <!--menu options-->
      <main>

        <!--section information-->
        <section id="inform">
          <div id="sobre">
            <h1>Freddy Quea</h1>
            <h2>Full-stack web and app developer</h2>
            <h3>UI/UX designer in training</h3>
            <h4>Always learning new things</h4>
          </div>

          <div id="codigo">
            <span>
              <pre class="hljs" style="display: block; overflow-x: auto; color: rgb(186, 186, 186);">let <span class="hljs-keyword" style="color: rgb(203, 120, 50);">button_menu </span>= document.querySelector(<span class="hljs-string" style="color: rgb(224, 196, 108);">".header_button"</span>)<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  let float_menu = document.querySelector(<span class="hljs-string" style="color: rgb(224, 196, 108);">".header_menu--float"</span>)<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                                          
                  let line_top = document.querySelector(<span class="hljs-string" style="color: rgb(224, 196, 108);">".header_button_line--top"</span>)<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  let line_under = document.querySelector(<span class="hljs-string" style="color: rgb(224, 196, 108);">".header_button_line--bottom"</span>)<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                                          
                  <span class="hljs-keyword" style="color: rgb(203, 120, 50);">button_menu.isSelected </span>= false<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                                          
                  function <span class="hljs-keyword" style="color: rgb(203, 120, 50);">addEffectWriting(element, </span>time) {
                      let element_array = element.innerText.split(<span class="hljs-string" style="color: rgb(224, 196, 108);">""</span>)<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  
                      element.count = <span class="hljs-number" style="color: rgb(104, 150, 186);">0</span><span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                      element.innerText = <span class="hljs-string" style="color: rgb(224, 196, 108);">""</span><span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  
                      function writeSymbols() {
                          element.innerText += element_array[element.count]<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                          element.count++<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  
                          if (element.count &lt;= element_array.length) {
                              setTimeout(() =&gt; {
                                  writeSymbols()<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                              }, time)<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                          } else if (element.count &gt;= element_array.length) {
                              element.count = <span class="hljs-number" style="color: rgb(104, 150, 186);">0</span><span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                              element.innerText = <span class="hljs-string" style="color: rgb(224, 196, 108);">""</span><span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  
                              writeSymbols()<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                          }
                      }
                      writeSymbols()<span class="hljs-comment" style="color: rgb(127, 127, 127);">;</span>
                  }</pre>
            </span>
          </div>
        </section>

        <!--section history-->
        <section id="historia">
          <img src="https://github.com/rqueaArequipa/rqueaArequipa.github.io/blob/main/img/log-main.png?raw=true"
            alt="QJ Developer">
          <h1>“Be nice to nerds. It is very likely that you will end up working for one of them.” <br> Bill Gates</h1>
        </section>

      </main>
    </div>
  </div>
  <div class="container">
    <footer class="py-3 my-4">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Home</a></li>
        <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Formularios</a></li>
        <li class="nav-item"><a href="#" class="nav-link px-2 text-white">Respuestas</a></li>
      </ul>
      <p class="text-center text-muted">&copy; 2023 QJ - Developer</p>
    </footer>
  </div>

</body>

</html>
