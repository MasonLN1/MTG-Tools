mtgconf <- function (wr, games){
  upper <- qbeta(0.975, wr*games+1, (1-wr)*games+1)
  lower <- qbeta(0.025, wr*games+1, (1-wr)*games+1)
  return ((upper-lower)/2)
}

mtgfullconf <- function (wins, losses){
  wr <- wins/(wins+losses)
  pmconf <- mtgconf(wr, wins+losses)
  print(paste0("Win rate: ", round(wr, digits=5)*100, "% +/- ", round(pmconf, digits=5)*100,"%"))
}