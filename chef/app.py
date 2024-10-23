from taipy.gui import Gui, navigate


def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

if __name__ == "__main__":
    root_md="<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2')]}|on_action=menu_option_selected|>"
    page1_md="## This is page 1"
    page2_md="## This is page 2"

    pages = {
        "/": root_md,
        "Page-1": page1_md,
        "Page-2": page2_md
    }

    Gui(pages=pages).run()