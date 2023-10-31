(function () {
    const modal = new bootstrap.Modal(document.getElementById("modal-logout"))
  
    htmx.on("htmx:afterSwap", (e) => {
      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "logout") {
        modal.show()
      }
    })
  
  
  })()