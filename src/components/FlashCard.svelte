<script lang="ts">
	import type { Line } from '../model/netzplan-data-interfaces';

	export let line: Line;

	let isFlipped = false;

	const toggleFlip = () => {
		isFlipped = !isFlipped;
	}
</script>

<style lang="scss">
  .blurred-card {
		width: 30rem;
    cursor: pointer;
  }

  .flash-card-inner.flipped {
    transform: rotateY(180deg);
		backface-visibility: hidden;
  }

  .flash-card-inner {
    height: 10rem;
    transition: transform 0.6s;
    transform-style: preserve-3d;
  }

  .flash-card-front,
	.flash-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.6s;
    transform-style: preserve-3d;
  }

  .flash-card-back {
    transform: rotateY(180deg);
		font-size: 1.2em;
		font-weight: 600;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	@media screen and (max-width: 576px) {
    .blurred-card {
      width: 20rem;
    }
  }
</style>

<button tabindex="0" class="blurred-card" on:click={toggleFlip}>
	<div class="flash-card-inner" class:flipped={isFlipped}>
		<div class="flash-card-front">
			<h2 class="line-label" style="background-color: {line.color}">{line.label}</h2>
		</div>
		<div class="flash-card-back">
			{#each line.basetacts as baseTact}
				<div class="base-tact">
					<div class="line-flow-stop">
						{baseTact.lineflowstops[0].station_label} ({baseTact.lineflowstops[0].departure_minute})
						-
						{baseTact.lineflowstops[baseTact.lineflowstops.length -1].station_label} ({baseTact.lineflowstops[baseTact.lineflowstops.length -1].arrival_minute})
					</div>
				</div>
			{/each}
		</div>
	</div>
</button>
