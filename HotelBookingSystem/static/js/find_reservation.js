(function () {
    const modal = new bootstrap.Modal(document.getElementById("find-reservation"))
  
    htmx.on("htmx:afterSwap", (e) => {
      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "find") {
        modal.show()
      }
    })
    htmx.on("htmx:beforeSwap", (e) => {
        // Empty response targeting #dialog => hide the modal
        if (e.detail.target.id == "find" && !e.detail.xhr.response) {
          modal.hide()
          e.detail.shouldSwap = false
        }
      })
    
      // Remove dialog content after hiding
      htmx.on("hidden.bs.modal", () => {
        document.getElementById("find").innerHTML = ""
      })
  
  })()