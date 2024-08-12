<script>
	import '../styles.scss'
</script>

<style lang="scss">
	#app {
    padding-inline: var(--inline-padding-header);
    margin-top: 2rem;
    padding-bottom: 2rem;
		height: calc(100vh - 5rem);
    background-image: url("../assets/background_netz-karte.jpg");
    background-size: contain;
    background-repeat: no-repeat;
		background-position: center;

		#title {
			font-weight: 600;
			letter-spacing: 0.1em;
			font-size: 1.1em;
		}
	}

	footer {
		position: fixed;
		bottom: 0.5rem;
		font-size: 0.9em;
		color: #797979;
		width: calc(100vw - 2 * var(--inline-padding-header));

		div {
			width: 100%;
			display: flex;
			justify-content: space-between;
		}
	}
</style>

<div id="app">
	<header>
		<span id="title">
			Train Line Trainer
		</span>
	</header>
	<main>
		<slot />
	</main>
	<footer>
		<div>
					<span id="last-data-update">
			Letztes Daten-Update: 12.08.2024
		</span>
			<span id="copyright">
				<a href="https://www.sbb.ch/">&copy; SBB CFF FFS</a>,
				<a href="https://github.com/david-lienberger/">David Lienberger</a>
		</span>
		</div>
	</footer>
</div>
