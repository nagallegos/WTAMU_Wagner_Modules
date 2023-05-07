function back() {
  let loc = String(window.location.href)
  //alert(loc.split("/submit")[0])
  
  window.location.href = loc.split("/submit")[0]
}
