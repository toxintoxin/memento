"use strict";(self.webpackChunkmemento=self.webpackChunkmemento||[]).push([[1375],{3128:(e,n,r)=>{r.r(n),r.d(n,{assets:()=>c,contentTitle:()=>o,default:()=>d,frontMatter:()=>t,metadata:()=>p,toc:()=>l});var s=r(4848),i=r(8453);const t={},o="shinyproxy",p={id:"shiny/shinyproxy",title:"shinyproxy",description:"\u81ea\u52a8\u751f\u6210shiny\u7684Dockerfile",source:"@site/docs/shiny/shinyproxy.md",sourceDirName:"shiny",slug:"/shiny/shinyproxy",permalink:"/memento/docs/shiny/shinyproxy",draft:!1,unlisted:!1,editUrl:"https://github.com/toxintoxin/memento/tree/main/docs/shiny/shinyproxy.md",tags:[],version:"current",frontMatter:{},sidebar:"shinySidebar",previous:{title:"shinyapps.io",permalink:"/memento/docs/shiny/shinyapps"}},c={},l=[{value:"\u81ea\u52a8\u751f\u6210shiny\u7684Dockerfile",id:"\u81ea\u52a8\u751f\u6210shiny\u7684dockerfile",level:2}];function a(e){const n={a:"a",code:"code",h1:"h1",h2:"h2",header:"header",img:"img",p:"p",pre:"pre",...(0,i.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(n.header,{children:(0,s.jsx)(n.h1,{id:"shinyproxy",children:"shinyproxy"})}),"\n",(0,s.jsx)(n.h2,{id:"\u81ea\u52a8\u751f\u6210shiny\u7684dockerfile",children:"\u81ea\u52a8\u751f\u6210shiny\u7684Dockerfile"}),"\n",(0,s.jsx)(n.p,{children:(0,s.jsx)(n.a,{href:"https://www.jumpingrivers.com/blog/shiny-auto-docker/",children:"https://www.jumpingrivers.com/blog/shiny-auto-docker/"})}),"\n",(0,s.jsx)(n.p,{children:"functions"}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{children:'glue_sys_reqs = function(pkgs) {\n  rlang::check_installed("curl")\n  rspm = Sys.getenv("RSPM_ROOT", "https://packagemanager.rstudio.com")\n  rspm_repo_id = Sys.getenv("RSPM_REPO_ID", 1)\n  rspm_repo_url = glue::glue("{rspm}/__api__/repos/{rspm_repo_id}")\n  \n  pkgnames = glue::glue_collapse(unique(pkgs), sep = "&pkgname=")\n  \n  req_url = glue::glue(\n    "{rspm_repo_url}/sysreqs?all=false",\n    "&pkgname={pkgnames}&distribution=ubuntu&release=22.04"\n  )\n  res = curl::curl_fetch_memory(req_url)\n  sys_reqs = jsonlite::fromJSON(rawToChar(res$content), simplifyVector = FALSE)\n  if (!is.null(sys_reqs$error)) rlang::abort(sys_reqs$error)\n\n  sys_reqs = purrr::map(sys_reqs$requirements, purrr::pluck, "requirements", "packages")\n  sys_reqs = sort(unique(unlist(sys_reqs)))\n  sys_reqs = glue::glue_collapse(sys_reqs, sep = " \\\\\\n    ")\n  glue::glue(\n    "RUN apt-get update -qq && \\\\ \\n",\n    "  apt-get install -y --no-install-recommends \\\\\\n    ",\n    sys_reqs,\n    "\\ && \\\\\\n",\n    "  apt-get clean && \\\\ \\n",\n    "  rm -rf /var/lib/apt/lists/*",\n    .trim = FALSE\n  )\n}\n\nshiny_write_docker = function(\n  path = ".", appdir = "app", lockfile = "shiny_renv.lock",\n  port = 3838, expose = TRUE, rspm = TRUE\n) {\n  rspm_env = ifelse(\n    rspm,\n    "ENV RENV_CONFIG_REPOS_OVERRIDE https://packagemanager.rstudio.com/cran/latest\\n",\n    ""\n  )\n  from_shiny_version = glue::glue("FROM rocker/shiny:{getRversion()}")\n  renv::snapshot(\n    project = path,\n    lockfile = lockfile,\n    prompt = FALSE,\n    force = TRUE\n  )\n  pkgs = renv::dependencies(appdir)$Package\n  sys_reqs = glue_sys_reqs(pkgs)\n  copy_renv = glue::glue("COPY {lockfile} renv.lock")\n  renv_install = \'RUN Rscript -e "install.packages(\\\'renv\\\')"\'\n  renv_restore  = \'RUN Rscript -e "renv::restore()"\'\n  \n  copy_app = glue::glue("COPY {appdir} /srv/shiny-server/")\n  expose = ifelse(expose, glue::glue("EXPOSE {port}"), "")\n  cmd = \'CMD ["/usr/bin/shiny-server"]\'\n  \n  ret = purrr::compact(list(\n    from_shiny_version,\n    rspm_env,\n    sys_reqs,\n    copy_renv,\n    renv_install,\n    renv_restore,\n    copy_app,\n    expose,\n    cmd\n  ))\n  readr::write_lines(ret, file = file.path(path, "Dockerfile"))\n}\n'})}),"\n",(0,s.jsx)(n.p,{children:"auto-generate dockerfile file"}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{children:'shiny_write_docker(path = ".", appdir = "app")\n'})}),"\n",(0,s.jsx)(n.p,{children:"build docker image"}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{children:"docker build -t your_image_name .\n"})}),"\n",(0,s.jsx)(n.p,{children:"test"}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{children:"docker run --rm -p 3838:3838 your_image_name\n"})}),"\n",(0,s.jsxs)(n.p,{children:["docker build issues\n",(0,s.jsx)(n.img,{alt:"Alt text",src:r(663).A+"",width:"1115",height:"628"})]}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{children:"docker build --no-cache -t your_image_name .\n"})})]})}function d(e={}){const{wrapper:n}={...(0,i.R)(),...e.components};return n?(0,s.jsx)(n,{...e,children:(0,s.jsx)(a,{...e})}):a(e)}},663:(e,n,r)=>{r.d(n,{A:()=>s});const s=r.p+"assets/images/image-a9210f2bdc8d86bc36db3b9aef38544f.png"},8453:(e,n,r)=>{r.d(n,{R:()=>o,x:()=>p});var s=r(6540);const i={},t=s.createContext(i);function o(e){const n=s.useContext(t);return s.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function p(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:o(e.components),s.createElement(t.Provider,{value:n},e.children)}}}]);